class MockTdlAdapter:

    def __init__(self):
        self.drawn_tiles = [] # array of tuples

    def draw(self, x, y, char, colour):
        self.drawn_tiles.append((x, y, char, colour))

    def flush(self):
        pass

    def calculate_fov(self, origin_x, origin_y, is_tile_walkable_callback, algorithm, view_radius, should_light_walls):
        # Mock the FOV tiles.
        light_radius = 5
        fov_tiles = []        

        for i in range(light_radius):
            fov_tiles.append((i, 0)) # horizontal ray
            fov_tiles.append((0, i)) # vertical ray

    def wait_for_input(self):
        return None

    # Ask for input. If none, returns None.
    def get_input(self):
        return None