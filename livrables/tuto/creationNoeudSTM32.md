# Comment créer une noeud à partir d'une carte STM32 

## Dépendances :
Pour Arch linux  :
- cmake
- arm-none-eabi-gcc
- arm-none-eabi-newlib
- openocd

## Projet 
``` Bash
git clone https://github.com/Lora-net/LoRaMac-node.git
cd LoRaMac-node/
git checkout master
mkdir build
cd buid
BOARD=B-L072Z-LRWAN1
cmake -DCMAKE_TOOLCHAIN_FILE="cmake/toolchain-arm-none-eabi.cmake" -DBOARD="$BOARD" -DAPPLICATION="LoRaMac" -DCLASS="classA" -DACTIVEREGION="LORAMAC_REGION_EU868" ..
make

```

## Sources

Documention d'un projet github : https://github.com/Lora-net/LoRaMac-node/blob/develop/Doc/development-environment.md