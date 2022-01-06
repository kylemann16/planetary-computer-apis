from typing import Dict, List

lidarclass_colormaps: Dict[str, Dict[int, List[int]]] = {
    "lidar-classification": {
        2: [139, 51, 38, 255],
        3: [143, 201, 157, 255],
        4: [5, 159, 43, 255],
        5: [47, 250, 11, 255],
        6: [209, 151, 25, 255],
        7: [232, 41, 7, 255],
        8: [197, 0, 204, 255],
        9: [26, 44, 240, 255],
        10: [165, 160, 173, 255],
        11: [81, 87, 81, 255],
        12: [203, 210, 73, 255],
        13: [209, 228, 214, 255],
        14: [160, 168, 231, 255],
        15: [220, 213, 164, 255],
        16: [214, 211, 143, 255],
        17: [151, 98, 203, 255],
        18: [236, 49, 74, 255],
        19: [185, 103, 45, 255],
        21: [58, 55, 9, 255],
        22: [76, 46, 58, 255],
        23: [20, 76, 38, 255],
        26: [78, 92, 32, 255]
    }

}

lidarreturns_colormaps: Dict[str, Dict[int, List[int]]] = {
    "lidar-returns": {
        0: [0, 0, 0, 255],
        1: [196, 73, 230, 255],
        2: [103, 145, 204, 255],
        3: [193, 237, 14, 255],
        4: [210, 63, 63, 255],
        5: [84, 218, 138, 255],
        6: [245, 130, 48, 255],
        7: [51, 141, 75, 255]
    }

}


lidarhag_colormaps: Dict[str, Dict[float, List[int]]] = {
    "lidar-hag": {
        -900.0: [0, 0, 0, 255],
        1.0: [0, 0, 0, 255],
        1.001: [0, 0, 128, 255],
        3.0: [0, 128, 0, 255],
        5.0: [255, 255, 255, 255],
        8.0: [255, 165, 0, 255],
        16.0: [255, 0, 0, 255],
        48.0: [255, 255, 255, 255]
    }

}

lidarintensity_colormaps: Dict[str, Dict[float, List[int]]] = {
    "lidar-intensity": {
        0: [255, 255, 255, 255],
        1: [238, 238, 238, 255],
        2: [221, 221, 221, 255],
        3: [204, 204, 204, 255],
        4: [187, 187, 187, 255],
        5: [170, 170, 170, 255],
        6: [153, 153, 153, 255],
        7: [136, 136, 136, 255],
        8: [119, 119, 119, 255],
        9: [102, 102, 102, 255],
        10: [85, 85, 85, 255],
        11: [68, 68, 68, 255],
        12: [50, 50, 50, 255],
        13: [33, 33, 33, 255],
        14: [16, 16, 16, 255],
        15: [0, 0, 0, 255]
    }
}

"""
Standard USGS LiDAR Classification color set (not complete)

2 139 51 38 255 Ground
3 143 201 157 255 Low Veg
4 5 159 43 255 Med Veg
5 47 250 11 255 High Veg
6 209 151 25 255 Building
7 232 41 7 255 Low Point
8 197 0 204 255 Reserved
9 26 44 240 255 Water
10 165 160 173 255 Rail
11 81 87 81 255 Road
12 203 210 73 255 Reserved
13 209 228 214 255 Wire - Guard (Shield)
14 160 168 231 255 Wire - Conductor (Phase)
15 220 213 164 255 Transmission Tower
16 214 211 143 255 Wire-Structure Connector (Insulator)
17 151 98 203 255 Bridge Deck
18 236 49 74 255 High Noise
19 185 103 45 255 Reserved
21 58 55 9 255 255 Reserved
22 76 46 58 255 255 Reserved
23 20 76 38 255 255 Reserved
26 78 92 32 255 255 Reserved
"""

