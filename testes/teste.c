#include <stdio.h>

int main() {
    float nota1, nota2, media; // Declara as variáveis para as notas e a média

    // Solicita a primeira nota ao usuário
    printf("Digite a primeira nota: ");
    scanf("%f", &nota1); // Lê a nota e armazena em nota1

    // Solicita a segunda nota ao usuário
    printf("Digite a segunda nota: ");
    scanf("%f", &nota2); // Lê a nota e armazena em nota2

    // Calcula a média, garantindo que a soma seja feita antes da divisão
    media = (nota1 + nota2) / 2.0;

    // Exibe a média calculada
    printf("A media das notas é: %.2f\n", media);

    return 0;
}
