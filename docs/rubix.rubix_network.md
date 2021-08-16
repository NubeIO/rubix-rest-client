<!-- markdownlint-disable -->

<a href="../rubix/rubix_network.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `rubix.rubix_network`






---

<a href="../rubix/rubix_network.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RubixNetwork`




<a href="../rubix/rubix_network.py#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(connection: RubixSession, global_uuid: str, master: bool = None)
```








---

<a href="../rubix/rubix_network.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_uuid`

```python
get_by_uuid(network_uuid: str, master: bool = None)
```

get network by its uuid slave/<g_uuid>/ps/api/generic/networks/uuid/<network_uuid> network_uuid: string master: bool :return: JSON 

---

<a href="../rubix/rubix_network.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_devices`

```python
get_devices(master: bool = None)
```

slave/<g_uuid>/ps/api/generic/devices list all rubix devices per rubix network :return: JSON 

---

<a href="../rubix/rubix_network.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_networks`

```python
get_networks(master: bool = None)
```

slave/<g_uuid>/ps/api/generic/networks list all rubix networks per edge device :return: JSON 

---

<a href="../rubix/rubix_network.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_points`

```python
get_points(master: bool = None)
```

slave/<g_uuid>/ps/api/generic/points list all rubix points per rubix device master: bool :return: JSON 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
