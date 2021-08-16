<!-- markdownlint-disable -->

<a href="../rubix/rubix_schedule.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `rubix.rubix_schedule`






---

<a href="../rubix/rubix_schedule.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RubixSchedule`




<a href="../rubix/rubix_schedule.py#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(connection: RubixSession, global_uuid: str, master: bool = None)
```








---

<a href="../rubix/rubix_schedule.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_name`

```python
get_by_name(schedule_name: str)
```

get a schedule by its name /ps/api/schedules/name/<schedule_name> schedule_name: string :return: JSON 

---

<a href="../rubix/rubix_schedule.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_uuid`

```python
get_by_uuid(schedule_uuid: str)
```

get a schedule by its name /ps/api/schedules/uuid/<schedule_uuid> schedule_name: string :return: JSON 

---

<a href="../rubix/rubix_schedule.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `master_get_all`

```python
master_get_all()
```

get schedules /ps/api/schedules :return: JSON 

---

<a href="../rubix/rubix_schedule.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `patch_by_name`

```python
patch_by_name(
    network_name: str,
    device_name: str,
    point_name: str,
    value: float,
    priority: int
)
```

write a point value by its names as in network, device and point names slave/<g_uuid>/ps/api/generic/points/name/<network_name>/<device_name>/<point_name> network_name: string device_name: string point_name: string value: float priority: int between 1 and 16 :return: JSON 

---

<a href="../rubix/rubix_schedule.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `patch_by_uuid`

```python
patch_by_uuid(point_uuid: str, value: float, priority: int)
```

write a point value by its uuid slave/<g_uuid>/ps/api/generic/points_value/uuid/<point_uuid> point_uuid: string value: float priority: int between 1 and 16 :return: JSON 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
