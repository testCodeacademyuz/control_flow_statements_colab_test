test_cases = {
    "taskOne": [
        {
            "input": [-1],
            "expected": -1
        },
        {
            "input": [1],
            "expected": 2
        },
        {
            "input": [9],
            "expected": 10
        },
        {
            "input": [3],
            "expected": 4
        },
        {
            "input": [-5],
            "expected": -5
        },
    ],
    "taskTwo": [
        {
            "input": [4],
            "expected": 5
        },
        {
            "input": [-1],
            "expected": -3
        },
        {
            "input": [10],
            "expected": 11
        },
    ],
    "taskThree": [
        {
            "input": [3],
            "expected": 4    
        },
        {
            "input": [0],
            "expected": 10
        },
        {
            "input": [-6],
            "expected": -8
        },
    ],
    "taskFour": [
        {
            "input": [1, 2, -3],
            "expected": 2
        },
        {
            "input": [1, 2, 3],
            "expected": 3
        },
        {
            "input": [-1, -2, -3],
            "expected": 0
        },
        {
            "input": [-4, -1, 2],
            "expected": 1
        },
    ],
    "taskFive": [
        {
            "input": [1, 2, 3],
            "expected": 0
        },
        {
            "input": [-1, -2, -3],
            "expected": 3
        },
        {
            "input": [-4, -1, 2],
            "expected": 2
        },
    ],
    "taskSix": [
        {
            "input": [1, 2, 3],
            "expected": "there are a lot of positive numbers"
        },
        {
            "input": [-1, -2, -3],
            "expected": "there are a lot of negative numbers"
        },
        {
            "input": [-4, -1, 2],
            "expected": "there are a lot of negative numbers"
        },
        {
            "input": [1, 2, -3],
            "expected": "there are a lot of positive numbers"
        },
    ],
    "taskSeven": [
        {
            "input": [25],
            "expected": "positive odd number"
        },
        {
            "input": [0],
            "expected": "the number is zero"
        },
        {
            "input": [-4],
            "expected": "negative even number"
        },
        {
            "input": [1],
            "expected": "positive odd number"
        },
        {
            "input": [-9],
            "expected": "negative odd number"
        },
        {
            "input": [10],
            "expected": "positive even number"
        }
    ],
    "taskEight": [
        {
            "input": [12],
            "expected": "two-digit even number"
        },
        {
            "input": [77],
            "expected": "two-digit odd number"
        },
        {
            "input": [123],
            "expected": "three-digit odd number"
        },
        {
            "input": [100],
            "expected": "three-digit even number"
        },
    ],
    "taskNine": [
        {
            "input": [54],
            "expected": True
        },
        {
            "input": [21],
            "expected": True
        },
        {
            "input": [12],
            "expected": False
        },
        {
            "input": [23],
            "expected": False
        },
    ],
    "taskTen": [
        {
            "input": [11],
            "expected": "Cold"
        },
        {
            "input": [21],
            "expected": "Normal"
        },
        {
            "input": [-1],
            "expected": "Freezing"
        },
        {
            "input": [31],
            "expected": "Hot"
        },
        {
            "input": [41],
            "expected": "Very Hot"
        },
        {
            "input": [2],
            "expected": "Very Cold"
        }
    ],
}