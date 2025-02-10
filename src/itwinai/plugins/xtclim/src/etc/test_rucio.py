import xarray as xr
from rucio.client import Client
rucio = Client()

listing = rucio.list_dids(
    scope="CMCC-ESM2", filters={"name": "tasmax_day_CMCC-ESM2_historical_r1i1p1f1_gn_*.nc"}, did_type="ALL", long=True
)

filelist = []
for ll in listing:
    replicas = rucio.list_replicas(
    dids=[{"scope": "CMCC-ESM2", "name": ll['name']}],
    schemes=[
        "file",
    ],
    )
    for replica in replicas:
        print(replica["scope"], replica["name"], replica["rses"]["DESY-DCACHE"][0])
    lfilepath=replica["rses"]["DESY-DCACHE"][0]
    filepath = lfilepath.replace('file://localhost', '')
    filelist.append(filepath)         

print(filelist)

tasmax = xr.open_mfdataset(filelist)

print(tasmax)
