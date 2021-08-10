<!-- markdownlint-disable -->

<a href="../rubix/rubix_slave_network.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `rubix.rubix_slave_network`






---

<a href="../rubix/rubix_slave_network.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RubixSlaveNetwork`




<a href="../rubix/rubix_slave_network.py#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(connection: RubixSession, global_uuid: str = None)
```








---

<a href="../rubix/rubix_slave_network.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_uuid`

```python
get_by_uuid(network_uuid: str)
```

get network by its uuid slave/<g_uuid>/ps/api/generic/networks/uuid/<network_uuid> network_uuid: string :return: JSON 

---

<a href="../rubix/rubix_slave_network.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_devices`

```python
get_devices()
```

slave/<g_uuid>/ps/api/generic/devices list all rubix devices per rubix network :return: JSON 

---

<a href="../rubix/rubix_slave_network.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_networks`

```python
get_networks()
```

slave/<g_uuid>/ps/api/generic/networks list all rubix networks per edge device :return: JSON 

---

<a href="../rubix/rubix_slave_network.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_points`

```python
get_points()
```

slave/<g_uuid>/ps/api/generic/points list all rubix points per rubix device :return: JSON 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
