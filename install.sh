#!/bin/bash

# Mostrar el contrato de licencia
zenity --text-info --title="License Agreement" --filename=LICENSE.txt --checkbox="I accept the terms and conditions."

# Verificar si el usuario aceptó el contrato
if [ $? -eq 0 ]; then
    # El usuario aceptó, proceder con la instalación
    echo "Installing MathSolver..."

    # Copiar los archivos a la ubicación deseada
    sudo cp -r MathSolver /opt/MathSolver

    # Verificar si el enlace simbólico ya existe
    if [ -f "/usr/local/bin/mathsolver" ]; then
        # Preguntar al usuario si desea sobrescribir el enlace
        zenity --question --title="MathSolver Installation" --text="A symbolic link already exists at /usr/local/bin/mathsolver. Do you want to overwrite it?"
        if [ $? -eq 0 ]; then
            # Sobrescribir el enlace
            sudo rm /usr/local/bin/mathsolver
            sudo ln -s /opt/MathSolver/run.py /usr/local/bin/mathsolver
            echo "Symbolic link overwritten."
        else
            echo "Installation completed without overwriting the symbolic link."
            exit 0
        fi
    else
        # Crear el enlace simbólico
        sudo ln -s /opt/MathSolver/run.py /usr/local/bin/mathsolver
        echo "Symbolic link created."
    fi

    echo "Installation completed."
else
    # El usuario no aceptó, cancelar la instalación
    echo "Installation canceled."
    exit 1
fi