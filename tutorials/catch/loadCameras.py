import numpy as np

def loadCameras( time, threshSurf, edgeLims, t2occ ):

    camera1 = {
        'number': 1,
        'port': 9001,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 1,
                'vertices': np.array(
                            [[   0,   0],
                             [  30,   0],
                             [  60, 150],
                             [   0, 150]]),
                'base_means': [118,123,127],
                'base_nEdges': 404,
                'base_nKeys': 11,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'meanThresh': 15,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 2,
                'vertices': np.array(
                            [[  90,   0],
                             [ 290,   0],
                             [ 230, 224],
                             [ 110, 224]]),
                'base_means': [117,117,115],
                'base_nEdges': 419,
                'base_nKeys': 18,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 15,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 3,
                'vertices': np.array(
                            [[ 310,   0],
                             [ 400,   0],
                             [ 400, 224],
                             [ 250, 224]]),
                'base_means': [119,119,117],
                'base_nEdges': 479,
                'base_nKeys': 3,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 15,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    camera2 = {
        'number': 2,
        'port': 9002,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 4,
                'vertices': np.array(
                            [[ 215,   0],
                             [ 370,   0],
                             [ 400, 100],
                             [ 400, 224],
                             [ 210, 224]]),
                'base_means': [126,126,125],
                'base_nEdges': 121,
                'base_nKeys': 4,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 5,
                'vertices': np.array(
                            [[  50,   0],
                             [ 200,   0],
                             [ 195, 224],
                             [   0, 224],
                             [   0, 170]]),
                'base_means': [130,130,131],
                'base_nEdges': 652,
                'base_nKeys': 35,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    camera3 = {
        'number': 3,
        'port': 9003,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 6,
                'vertices': np.array(
                            [[ 280,   0],
                             [ 380,   0],
                             [ 400,  35],
                             [ 400, 224],
                             [ 330, 224]]),
                'base_means': [102,102,101],
                'base_nEdges': 4,
                'base_nKeys': 1,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 7,
                'vertices': np.array(
                            [[ 130,   0],
                             [ 265,   0],
                             [ 310, 224],
                             [ 105, 224]]),
                'base_means': [122,123,121],
                'base_nEdges': 152,
                'base_nKeys': 11,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 8,
                'vertices': np.array(
                            [[  20,   0],
                             [ 115,   0],
                             [  85, 224],
                             [   0, 224],
                             [   0,  40]]),
                'base_means': [137,137,140],
                'base_nEdges': 730,
                'base_nKeys': 43,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    camera4 = {
        'number': 4,
        'port': 9004,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 9,
                'vertices': np.array(
                            [[ 275,  30],
                             [ 335,  30],
                             [ 400, 115],
                             [ 400, 224],
                             [ 390, 224]]),
                'base_means': [120,121,119],
                'base_nEdges': 67,
                'base_nKeys': 2,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 10,
                'vertices': np.array(
                            [[ 165,  30],
                             [ 260,  30],
                             [ 370, 224],
                             [ 240, 224]]),
                'base_means': [121,122,119],
                'base_nEdges': 67,
                'base_nKeys': 2,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 11,
                'vertices': np.array(
                            [[  40,  30],
                             [ 150,  30],
                             [ 220, 224],
                             [  40, 224]]),
                'base_means': [119,119,119],
                'base_nEdges': 391,
                'base_nKeys': 12,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    camera5 = {
        'number': 5,
        'port': 9005,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 12,
                'vertices': np.array(
                            [[ 310,   0],
                             [ 400,   0],
                             [ 400, 224],
                             [ 360, 224]]),
                'base_means': [99,101,103],
                'base_nEdges': 2,
                'base_nKeys': 1,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 13,
                'vertices': np.array(
                            [[ 135,   0],
                             [ 290,   0],
                             [ 330, 224],
                             [  85, 224]]),
                'base_means': [122,122,121],
                'base_nEdges': 405,
                'base_nKeys': 24,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 14,
                'vertices': np.array(
                            [[  20,   0],
                             [ 115,   0],
                             [  60, 224],
                             [   0, 224],
                             [   0,  30]]),
                'base_means': [119,119,121],
                'means': [0,0,0],
                'base_nEdges': 650,
                'base_nKeys': 25,
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    camera6 = {
        'number': 6,
        'port': 9006,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 15,
                'vertices': np.array(
                            [[   0,  40],
                             [  40,  40],
                             [ 110, 140],
                             [   0, 120]]),
                'base_means': [115,113,113],
                'base_nEdges': 53,
                'base_nKeys': 1,
                'base_means': [114,113,113],
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 16,
                'vertices': np.array(
                            [[  85,  20],
                             [ 290,  20],
                             [ 235, 170],
                             [ 140, 170]]),
                'base_means': [110,113,113],
                'base_nEdges': 115,
                'base_nKeys': 16,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 17,
                'vertices': np.array(
                            [[ 365,   0],
                             [ 400,   0],
                             [ 400,  85],
                             [ 370, 120],
                             [ 290, 125]]),
                'base_means': [109,111,111],
                'base_nEdges': 58,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 22,
                'vertices': np.array(
                            [[ 150, 200],
                             [ 275, 200],
                             [ 255, 230],
                             [ 155, 225]]),
                'base_means': [166,163,163],
                'base_nEdges': 122,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
        ]
    }
    cameras = {1: camera1,
               2: camera2,
               3: camera3,
               4: camera4,
               5: camera5,
               6: camera6}
    
    return cameras
