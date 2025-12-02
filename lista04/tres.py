"""Supondo que a população de um país X seja da ordem de 70.000 habitantes com uma taxa
anual de crescimento de 3.5% e que a população de Y seja 180.000 habitantes com uma
taxa de crescimento de 1.5%. Escreva um programa que calcule e escreva o número de
anos necessários para que a população do país X ultrapasse ou iguale a população do país
Y, mantidas as taxas de crescimento. 
"""
popx=70000
popy=180000
anos=0
while popx<=popy:
    popanx=popx*0.035
    popany=popy*0.015
    popx+=popanx
    popy+=popany
    anos+=1
print(f"a população de x vai passar a de y em {anos}")