# Recomendaciones
- Por motivos de seguridad, para ejecutar este proyecto necesitas usar un **Entorno Virtual**, ya que se le harán modificaciones a las dependencias nativas de Python, las cuales son esenciales para el funcionamiento de Linux, así que se harán las modificaciones en un entorno virtual para evitar romper alguna parte importante del   SO.
## Pasos para activar el entorno virtual.
	1.  En tu terminal ejecuta:
    		python3 -m venv ml_lang
	Esto creará el entorno virtual.
	
	2. Luego activalo con:
```python
source ml_lang/bin/activate
```
	3. Revisa las dependencias necesarias en el archivo requirements.txt e instalalo con:
```python
pip install -r requirements.txt
```
	4. Cuando hayas terminado de ejecutar el proyecto, puedes desactivar el entorno con:
```python
deactivate
```
Esto regresará al Python nativo de tu sistema.