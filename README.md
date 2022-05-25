# StreetCompleteNumbers

StreetCompleteNumbers is a python script to get the number of solved [StreetComplete](https://github.com/streetcomplete/StreetComplete)-Quests for a user ny querying [OpenStreetMap API](https://wiki.openstreetmap.org/wiki/API_v0.6).

## Usage

Call the function StreetCompleteNumbers after importing with a [OSM](https://osm.org)-username as the parameter. The function also accepts an int as a second optional _maximum_ parameter, that if set will make the script stop getting more than ( _maximum_ * 100 ) changesets.

```python
from StreetCompleteNumbers import StreetCompleteNumbers
StreetCompleteNumbers("maxmustermann")
```

## Example Output
The function returns a tuple with the total number of solved quests (seen as ★ in StreetComplete) as first value and a JSON-Object containing the solved quest numbers for every quest type. 

```
(31549, {'AddMaxSpeed': 231, 'DetermineRecyclingGlass': 29, 'AddRecyclingType': 44, 'AddFootwayPartSurface': 71, 'AddCyclewayPartSurface': 68, 'AddAddressStreet': 30, 'AddHousenumber': 129, 'AddCycleway': 455, 'AddMaxWeight': 28, 'AddParkingFee': 131, 'AddParkingType': 184, 'AddParkingAccess': 209, 'AddPostboxCollectionTimes': 75, 'AddPlaygroundAccess': 85, 'AddRecyclingContainerMaterials': 58, 'AddTrafficSignalsButton': 82, 'AddTrafficSignalsVibration': 102, 'AddTrafficSignalsSound': 93, 'AddVegetarian': 75, 'AddOpeningHours': 450, 'AddPlaceName': 98, 'AddWheelchairAccessBusiness': 307, 'AddVegan': 35, 'AddBenchBackrest': 245, 'AddSidewalk': 511, 'AddStepCount': 290, 'AddHandrail': 297, 'AddStepsIncline': 259, 'AddStepsRamp': 315, 'AddPathSurface': 2983, 'AddForestLeafType': 65, 'AddRoadSurface': 987, 'AddLanes': 204, 'AddRoofShape': 4189, 'AddBuildingLevels': 6030, 'AddBuildingType': 8146, 'AddTactilePavingCrosswalk': 155, 'AddCrossingIsland': 58, 'AddCrossingType': 76, 'AddBollardType': 12, 'AddToiletsFee': 6, 'AddWheelchairAccessToilets': 9, 'AddRailwayCrossingBarrier': 18, 'AddInternetAccess': 15, 'AddGeneralFee': 5, 'AddRoadName': 58, 'AddPitchSurface': 22, 'AddBusStopShelter': 42, 'AddBenchStatusOnBusStop': 44, 'AddTactilePavingBusStop': 78, 'CheckExistence': 325, 'AddTracktype': 31, 'AddMaxHeight': 63, 'AddWayLit': 2521, 'AddBusStopLit': 40, 'AddBikeParkingType': 18, 'AddCyclewaySegregation': 83, 'AddProhibitedForPedestrians': 18, 'AddPitchLit': 19, 'AddBikeParkingFee': 1, 'AddBikeParkingCapacity': 34, 'AddClothingBinOperator': 17, 'AddFireHydrantType': 4, 'AddChargingStationOperator': 11, 'AddChargingStationCapacity': 10, 'AddBabyChangingTable': 5, 'AddBikeParkingCover': 26, 'AddBoardType': 21, 'AddBikeParkingAccess': 1, 'SpecifyShopType': 1, 'AddBarrierType': 1, 'MarkCompletedHighwayConstruction': 16, 'AddAtmOperator': 3, 'AddPowerPolesMaterial': 42, 'AddBusStopName': 3, 'AddSummitRegister': 1, 'AddBridgeStructure': 8, 'AddSport': 11, 'AddCarWashType': 4, 'CheckShopType': 5, 'MarkCompletedBuildingConstruction': 3, 'AddSuspectedOneway': 3, 'AddToiletAvailability': 1, 'AddOneway': 2, 'AddInformationToTourism': 3, 'AddWheelchairAccessOutside': 1, 'AddKerbHeight': 1, 'AddTactilePavingKerb': 1, 'AddMotorcycleParkingCover': 2, 'AddFerryAccessMotorVehicle': 1})
```
