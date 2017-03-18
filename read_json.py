import json
from pprint import pprint

JSON_DATA = {
  "geocoded_waypoints": [
    {
      "geocoder_status": "OK",
      "place_id": "ChIJn8N5VRvZxkcRmLlkgWTSmvM",
      "types": [
        "locality",
        "political"
      ]
    },
    {
      "geocoder_status": "OK",
      "place_id": "ChIJA1KH-2HaxkcRmexWrH6ks6A",
      "types": [
        "locality",
        "political"
      ]
    }
  ],
  "routes": [
    {
      "bounds": {
        "northeast": {
          "lat": 51.445833,
          "lng": 5.4699119
        },
        "southwest": {
          "lat": 51.4175293,
          "lng": 5.403431400000001
        }
      },
      "copyrights": "Map data ©2017 Google",
      "legs": [
        {
          "distance": {
            "text": "7.0 km",
            "value": 7012
          },
          "duration": {
            "text": "14 mins",
            "value": 824
          },
          "end_address": "Veldhoven, Netherlands",
          "end_location": {
            "lat": 51.4175293,
            "lng": 5.406064
          },
          "start_address": "Eindhoven, Netherlands",
          "start_location": {
            "lat": 51.4416143,
            "lng": 5.469695700000001
          },
          "steps": [
            {
              "distance": {
                "text": "0.6 km",
                "value": 628
              },
              "duration": {
                "text": "2 mins",
                "value": 98
              },
              "end_location": {
                "lat": 51.4451158,
                "lng": 5.4631497
              },
              "html_instructions": "Head <b>east</b> on <b>PSV-laan</b> toward <b>Vonderweg</b>",
              "polyline": {
                "points": "ae~xHshk`@BMCEEEEGEGEPELITKVcB|EwChJcAfCq@rAkCzEq@`A_@r@Sl@ELCJ[z@"
              },
              "start_location": {
                "lat": 51.4416143,
                "lng": 5.469695700000001
              },
              "travel_mode": "DRIVING"
            },
            {
              "distance": {
                "text": "0.2 km",
                "value": 234
              },
              "duration": {
                "text": "1 min",
                "value": 30
              },
              "end_location": {
                "lat": 51.4436693,
                "lng": 5.461028
              },
              "html_instructions": "Turn <b>left</b> onto <b>Glaslaan</b>",
              "maneuver": "turn-left",
              "polyline": {
                "points": "_{~xHu_j`@GTDLFLLXLXT`@HPNLJJFBD@H?L@j@n@nBpC@h@"
              },
              "start_location": {
                "lat": 51.4451158,
                "lng": 5.4631497
              },
              "travel_mode": "DRIVING"
            },
            {
              "distance": {
                "text": "0.6 km",
                "value": 578
              },
              "duration": {
                "text": "1 min",
                "value": 69
              },
              "end_location": {
                "lat": 51.4458176,
                "lng": 5.453551699999999
              },
              "html_instructions": "Continue onto <b>Kastanjelaan</b>",
              "polyline": {
                "points": "}q~xHmri`@@R?\\?JAHAPOr@U`Am@~Bg@pBy@rDkA`FERKb@ADER?BEVAFA@WvAe@nBIZq@rCMz@Af@Bj@"
              },
              "start_location": {
                "lat": 51.4436693,
                "lng": 5.461028
              },
              "travel_mode": "DRIVING"
            },
            {
              "distance": {
                "text": "0.3 km",
                "value": 337
              },
              "duration": {
                "text": "1 min",
                "value": 58
              },
              "end_location": {
                "lat": 51.4451208,
                "lng": 5.448835799999999
              },
              "html_instructions": "Continue onto <b>Cederlaan</b>",
              "polyline": {
                "points": "k__yHuch`@@LBf@Df@^bDPbBRbBNzAJlABNFfAB^HjA@T@V?R?H?R?T"
              },
              "start_location": {
                "lat": 51.4458176,
                "lng": 5.453551699999999
              },
              "travel_mode": "DRIVING"
            },
            {
              "distance": {
                "text": "2.6 km",
                "value": 2567
              },
              "duration": {
                "text": "5 mins",
                "value": 286
              },
              "end_location": {
                "lat": 51.4327845,
                "lng": 5.418362699999999
              },
              "html_instructions": "At the roundabout, take the <b>3rd</b> exit onto <b>Noord Brabantlaan</b>",
              "maneuver": "roundabout-right",
              "polyline": {
                "points": "_{~xHgfg`@A@A@A@A@A@A@?@ABABABABAB?BAB?D?B?B?D?B?B@D?B@B@B?BBF@??@@@@@@@@@@@@??@@?@@@?@@HTFRDJFRJ\\Fh@Jv@Hn@@JJt@^tBlAjGPdABN?BH`@Hh@@BBTz@dEf@~BJTjArD|@pCL^DNFNFPTn@fGfR\\tA\\bA^lAFNDNDLBJf@pAJXDNvA`EvA`Ej@jBh@jBNh@Rn@`@xAzAhF^nANd@Tn@Nd@HXVbAz@jDBHBHJj@Jh@FZHd@BN?@Lx@@BNdADVFh@Hh@Jv@Jv@BL?FBL@FBH@HP~@N~@Nl@Tz@Rl@\\v@NVJTDJFJFJZh@jAdBj@|@t@hAfBpCRZh@v@b@p@TXZd@jA`BDFDF"
              },
              "start_location": {
                "lat": 51.4451208,
                "lng": 5.448835799999999
              },
              "travel_mode": "DRIVING"
            },
            {
              "distance": {
                "text": "1.3 km",
                "value": 1345
              },
              "duration": {
                "text": "2 mins",
                "value": 96
              },
              "end_location": {
                "lat": 51.42455529999999,
                "lng": 5.4045068
              },
              "html_instructions": "Continue onto <b>Heerbaan</b>",
              "polyline": {
                "points": "{m|xHwga`@lAhBlAfBdErGfErGrBvC\\j@l@z@dBfCNRNRDFBDV^pAlB`AxAl@~@p@fAp@hAz@dB|@lBdAtCl@jBn@zBt@|Cb@zBz@rF"
              },
              "start_location": {
                "lat": 51.4327845,
                "lng": 5.418362699999999
              },
              "travel_mode": "DRIVING"
            },
            {
              "distance": {
                "text": "0.4 km",
                "value": 376
              },
              "duration": {
                "text": "1 min",
                "value": 48
              },
              "end_location": {
                "lat": 51.4223454,
                "lng": 5.405180400000001
              },
              "html_instructions": "At the roundabout, take the <b>3rd</b> exit onto <b>Heemweg</b>",
              "maneuver": "roundabout-right",
              "polyline": {
                "points": "ozzxHeq~_@GJGJGLCNCPAPAPB\\@B?@?B@@?B@@?@@DDJFJHJHFHDJ@H?NE@?@A@ABA@?@A@A@AFKFKDKBOBO@O?OAO`@Q@Ab@UTKTMp@]p@]JEfAi@BCFGV["
              },
              "start_location": {
                "lat": 51.42455529999999,
                "lng": 5.4045068
              },
              "travel_mode": "DRIVING"
            },
            {
              "distance": {
                "text": "0.6 km",
                "value": 627
              },
              "duration": {
                "text": "1 min",
                "value": 86
              },
              "end_location": {
                "lat": 51.4185913,
                "lng": 5.4101069
              },
              "html_instructions": "At the roundabout, take the <b>2nd</b> exit and stay on <b>Heemweg</b><div style=\"font-size:0.9em\">Go through 2 roundabouts</div>",
              "maneuver": "roundabout-right",
              "polyline": {
                "points": "ulzxHku~_@B@D@D@DADADEBCBEBE@K?O?GAGCIACH_@BK@I@SBe@@a@BgB@_@?UBSD[H]HWHOHSPQfAeA@B@BD@DBB@DABABCBEBE@E@E?I?GACzBoBzBoB@@BBB@D@DAB?BCBCBC@G@E?E?I?If@a@VOZQLENEPAX?L@JBF@F@"
              },
              "start_location": {
                "lat": 51.4223454,
                "lng": 5.405180400000001
              },
              "travel_mode": "DRIVING"
            },
            {
              "distance": {
                "text": "0.3 km",
                "value": 268
              },
              "duration": {
                "text": "1 min",
                "value": 44
              },
              "end_location": {
                "lat": 51.4176509,
                "lng": 5.406791399999999
              },
              "html_instructions": "At the roundabout, take the <b>1st</b> exit and stay on <b>Heemweg</b>",
              "maneuver": "roundabout-right",
              "polyline": {
                "points": "euyxHet_`@?F?D?DBD@DBBDDD?D?B?DCDHHJLRFNJRFVFXDZFf@N`BJx@B\\BXLxALxABP@R"
              },
              "start_location": {
                "lat": 51.4185913,
                "lng": 5.4101069
              },
              "travel_mode": "DRIVING"
            },
            {
              "distance": {
                "text": "52 m",
                "value": 52
              },
              "duration": {
                "text": "1 min",
                "value": 9
              },
              "end_location": {
                "lat": 51.4175293,
                "lng": 5.406064
              },
              "html_instructions": "Continue onto <b>Bossebaan</b>",
              "polyline": {
                "points": "ioyxHm__`@@LBLPtB"
              },
              "start_location": {
                "lat": 51.4176509,
                "lng": 5.406791399999999
              },
              "travel_mode": "DRIVING"
            }
          ],
          "traffic_speed_entry": [],
          "via_waypoint": []
        }
      ],
      "overview_polyline": {
        "points": "ae~xHshk`@BMCEKMEGEPOb@oBtFwChJcAfCq@rAkCzEq@`A_@r@Yz@_@fAGTDLTf@b@z@X^RNN@L@j@n@nBpC@h@@p@ATQdAcA`EsDzOu@zDo@jCq@rCMz@@rADt@jArKf@`GPxC?fAKLK`@Bb@JTJHLV`@pA^|Cj@jD~ApIV~ADXbBdIbDzJj@`BfGfR\\tA|@pCVx@pC|HbClHx@tCpDbM~@tCzAbGh@vCp@vEn@nEr@vDh@hBl@nA`@x@hEvGhEvGbChDfJlNfErGrBvCjAfBjCvDnDlF~AfClBnD|@lBdAtC|AfFxAxGz@rFGJOXG`@Cb@D`@@JHTPVRLT@PEHELQLWF_@@_@AO`@Qd@Wj@YvDkBJKV[B@JBJCPU@[AOEMLk@HeBDgCBi@Ny@Rg@Ze@fAeA@BFDHDHCFIDK@OAKvF_FNHHAFGDK@K?S~@q@h@W`@Gf@@RDF@?F?JNTJ?HCd@x@Rj@Lt@f@`F|@dK"
      },
      "summary": "Noord Brabantlaan",
      "warnings": [],
      "waypoint_order": []
    }
  ],
  "status": "OK"
}

def get_duration(self):
	return JSON_DATA["routes"][0]["legs"][0]["duration"]["text"] #14 mins