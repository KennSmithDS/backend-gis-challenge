request_body_200 = {
	"type": "Feature",
	"properties": {},
	"geometry": {
		"coordinates": [
			[
				[
					0, 0
				],
				[
					0, 1
				],
				[
					1, 1
				],
				[
					1, 0
				],
				[
					0, 0
				]
			]
		],
		"type": "Polygon"
	}
}

response_body_200 = {
	"type": "Feature",
	"geometry": {
		"coordinates": [
			[
				[
					0,
					0
				],
				[
					0,
					1
				],
				[
					1,
					1
				],
				[
					1,
					0
				],
				[
					0,
					0
				]
			]
		],
		"type": "Polygon"
	},
	"properties": {
		"area": {
			"value": 12392658216.37442,
			"unit": "sq meters"
		},
		"centroid": {
			"type": "Point",
			"coordinates": [
				0.5,
				0.5
			]
		}
	},
	"bbox": [
		0,
		0,
		1,
		1
	]
}

request_body_not_feature = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
              "coordinates": [
                [
                  [
                    0,
                    0
                  ],
                  [
                    0,
                    1
                  ],
                  [
                    1,
                    1
                  ],
                  [
                    1,
                    0
                  ],
                  [
                    0,
                    0
                  ]
                ]
              ],
                "type": "Polygon"
            }
        }
    ]
}

request_body_not_poly = {
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          [-105.0, 25.0],
          [-105.0, 27.5],
          [-102.5, 27.5],
          [-102.5, 25.0],
          [-105.0, 25.0]
        ]
      ],
      [
        [
          [-102.5, 25.0],
          [-102.5, 27.5],
          [-100.0, 27.5],
          [-100.0, 25.0],
          [-102.5, 25.0]
        ]
      ],
      [
        [
          [-105.0, 27.5],
          [-105.0, 30.0],
          [-102.5, 30.0],
          [-102.5, 27.5],
          [-105.0, 27.5]
        ]
      ],
      [
        [
          [-102.5, 27.5],
          [-102.5, 30.0],
          [-100.0, 30.0],
          [-100.0, 27.5],
          [-102.5, 27.5]
        ]
      ]
    ]
  },
  "properties": {}
}
    
request_body_not_multipoly = {
  "type": "Feature",
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [
      [
        [-105.0, 25.0],
        [-105.0, 30.0],
        [-100.0, 30.0],
        [-100.0, 25.0],
        [-105.0, 25.0]
      ]
    ]
  },
  "properties": {}
}