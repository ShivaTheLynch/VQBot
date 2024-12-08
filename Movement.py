class Movement:
        def FollowPath(path_handler, follow_handler, log_actions=False):
            """
            Purpose: Follow a path using the path handler and follow handler objects.
            Args:
                path_handler (PathHandler): The PathHandler object containing the path coordinates.
                follow_handler (FollowXY): The FollowXY object for moving to waypoints.
            Returns: None
            """
            if follow_handler.is_following():
                follow_handler.update()
                return

            current_position = Player.GetXY()
            point = path_handler.advance(current_position)
            if point is not None:
                follow_handler.move_to_waypoint(point[0], point[1])
                if log_actions:
                    Py4GW.Console.Log("FollowPath", f"Moving to {point}", Py4GW.Console.MessageType.Info)

        def IsFollowPathFinished(path_handler, follow_handler):
            return path_handler.is_finished() and follow_handler.has_arrived()


        class FollowXY:
            def __init__(self, tolerance=100):
                """
                Initialize the FollowXY object with default values.
                Routine for following a waypoint.
                """
                self.waypoint = (0, 0)
                self.tolerance = tolerance
                self.player_instance = PyPlayer.PyPlayer()
                self.following = False
                self.arrived = False
                self.timer = Py4GW.Timer()  # Timer to track movement start time
                self.wait_timer = Py4GW.Timer()  # Timer to track waiting after issuing move command
                self.wait_timer_run_once = True

            def calculate_distance(self, pos1, pos2):
                """
                Calculate the Euclidean distance between two points.
                """
                return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

            def move_to_waypoint(self, x, y, tolerance=None):
                """
                Move the player to the specified coordinates.
                Args:
                    x (float): X coordinate of the waypoint.
                    y (float): Y coordinate of the waypoint.
                    tolerance (int, optional): The distance threshold to consider arrival. Defaults to the initialized value.
                """
                self.reset()
                self.waypoint = (x, y)
                self.tolerance = tolerance if tolerance is not None else self.tolerance
                self.following = True
                self.arrived = False
                self.player_instance.Move(x, y)
                self.timer.start()

            def reset(self):
                """
                Cancel the current move command and reset the waypoint following state.
                """
                self.following = False
                self.arrived = False
                self.timer.reset()
                self.wait_timer.reset()

            def update(self):
                """
                Update the FollowXY object's state, check if the player has reached the waypoint,
                and issue new move commands if necessary.
                """
                if self.following:
                    current_position = Player.GetXY()
                    is_casting = Agent.IsCasting(Player.GetAgentID())
                    is_moving = Agent.IsMoving(Player.GetAgentID())
                    is_knocked_down = Agent.IsKnockedDown(Player.GetAgentID())

                    # Check if the wait timer has elapsed and re-enable movement checks
                    if self.wait_timer.has_elapsed(1500):
                        self.wait_timer.reset()
                        self.wait_timer_run_once = True

                    # Check if the player has arrived at the waypoint
                    if self.calculate_distance(current_position, self.waypoint) <= self.tolerance:
                        self.arrived = True
                        self.following = False
                        return

                    if is_casting or is_moving or is_knocked_down:
                        return 

                    # Re-issue the move command if the player is not moving and not casting
                    if self.wait_timer_run_once:
                        # Use the move_to_waypoint function to reissue movement
                        Player.Move(0,0) #reset movement pointer?
                        Player.Move(self.waypoint[0], self.waypoint[1])
                        self.wait_timer_run_once  = False  # Disable immediate re-issue
                        self.wait_timer.start()  # Start the wait timer to prevent spamming movement
                        Py4GW.Console.Log("FollowXY", f"stopped, reissue move", Py4GW.Console.MessageType.Info)

            def get_time_elapsed(self):
                """
                Get the elapsed time since the player started moving.
                """
                return self.timer.get_elapsed_time()

            def get_distance_to_waypoint(self):
                """
                Get the distance between the player and the current waypoint.
                """
                current_position = Player.GetXY()
                return self.calculate_distance(current_position, self.waypoint)

            def is_following(self):
                """
                Check if the player is currently following a waypoint.
                """
                return self.following

            def has_arrived(self):
                """
                Check if the player has arrived at the current waypoint.
                """
                return self.arrived


        class PathHandler:
            def __init__(self, coordinates, tolerance=100):
                """
                Purpose: Initialize the PathHandler with a list of coordinates.
                Args:
                    coordinates (list): A list of tuples representing the points (x, y).
                Returns: None
                """
                self.coordinates = coordinates
                self.tolerance = tolerance
                self.visited = [False] * len(coordinates)  # Track visited points
                self.index = 0
                self.reverse = False  # By default, move forward
                self.finished = False

            def get_current_point(self):
                """
                Purpose: Get the current point in the list of coordinates.
                Args: None
                Returns: tuple or None
                """
                if not self.coordinates or self.finished:
                    return None
                return self.coordinates[self.index]

            # Helper function to calculate distance
            def calculate_distance(self, pos1, pos2):
                return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5
            
            def advance(self, current_position):
                """
                Returns the next target point based on the path and updates the visited status.
                If the current point is reached within tolerance, it marks it as visited and advances.
                """
                if self.index >= len(self.coordinates):
                    return None  # All points have been visited

                # If we are at the start (index 0), find the closest point
                if self.index == 0:
                    closest_index = 0
                    closest_distance = self.calculate_distance(current_position, self.coordinates[0])
                    
                    for i in range(1, len(self.coordinates)):
                        distance = self.calculate_distance(current_position, self.coordinates[i])
                        if distance < closest_distance:
                            closest_distance = distance
                            closest_index = i

                    self.index = closest_index  # Set index to the closest point

                current_point = self.coordinates[self.index]
                
                # Check if we've reached the current point
                if self.calculate_distance(current_position, current_point) <= self.tolerance:
                    self.visited[self.index] = True

                    if self.index < len(self.coordinates) - 1:
                        self.index += 1
                    else:
                        self.finished = True

                    # If there's a next point, return it; otherwise, return None
                    if self.index < len(self.coordinates):
                        return self.coordinates[self.index]
                
                return current_point  # Still need to move to the current point

            def toggle_direction(self):
                """
                Purpose: Manually reverse the current direction of traversal.
                Args: None
                Returns: None
                """
                self.reverse = not self.reverse

            def reset(self):
                """
                Purpose: Reset the path traversal to the start or end depending on direction.
                Args: None
                Returns: None
                """
                self.index = 0 if not self.reverse else len(self.coordinates) - 1
                self.finished = False

            def is_finished(self):
                """
                Purpose: Check if the traversal has finished.
                Args: None
                Returns: bool
                """
                return self.finished

            def set_position(self, index):
                """
                Purpose: Set the current index in the list of coordinates.
                Args:
                    index (int): The index to set the position to.
                Returns: None
                """
                if 0 <= index < len(self.coordinates):
                    self.index = index
                    self.finished = False
                else:
                    raise IndexError(f"Index {index} out of bounds for coordinates list")

            def get_position(self):
                """
                Purpose: Get the current index in the list of coordinates.
                Args: None
                Returns: int
                """
                return self.index