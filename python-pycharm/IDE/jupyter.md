卸载
使用
pip uninstall jupyter

是卸不掉jupyter的
1 
(virenv)~/ pip install pip-autoremove
2  
(virenv)~/ pip-autoremove jupyter -y
pip-autoremove会卸载掉package和无用的依赖
