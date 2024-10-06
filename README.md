# Data Code Challenge

## Objective

Extract and transform specific data from a fire extinguisher verification registry document into a structured CSV file.

## Challenge Description

You are provided with an Excel document containing verification records of fire extinguishers. Your task is to write a Python script that processes this document and extracts the required fields into a CSV file. The CSV file should follow a specific format with defined headers.

## Input

A multi-line string containing the verification records of fire extinguishers. The document includes static information (such as company name, date, and client number) at the top, followed by a table with detailed records of each fire extinguisher.

## Output

A CSV file with the following headers:

EMPRESA, FECHA, CLIENTE_N, TIPO, N_IDENTIFICACION, CARGA, PESO, ZONA, PRESION, REVISION, FECHA_P_H, VTO_B, OBSERVACIONES


### Example Output

The resulting CSV should look like this:

EMPRESA,FECHA,CLIENTE_N,TIPO,N_IDENTIFICACION,CARGA,PESO,ZONA,PRESION,REVISION,FECHA_P_H,VTO_B,OBSERVACIONES Ejemplo 1,10/30/18,605003,PS9,5003/1 76935,OK,OK 13,450,,15kgcm2,OCTUBRE,10-18,OK,P.H. Ejemplo 1,10/30/18,605003,PS6,5003/2 1751,OK,OK 9,400,,15kgcm2,OCTUBRE,10-14,OK, ... ...


## Additional Information

- You may use regular expressions or any other string manipulation techniques to extract the data.
- Ensure that the script handles potential irregularities in the input format gracefully.
- The use of any machine learning models or external libraries is optional but not required for this task.

Good luck, and happy coding!
