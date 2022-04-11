/*
 * @Author: JIANG Yilun
 * @Date: 2022-03-24 15:32:52
 * @LastEditTime: 2022-03-24 16:03:31
 * @LastEditors: JIANG Yilun
 * @Description:
 * @FilePath: /UGA_INF/INF203/Language C/semaine 7/TP7/lecture_fich.c
 */
#include <stdio.h>

int main()
{
	FILE *f;
	char c;

	f = fopen("Candide_chapitre1.txt", "r");
	if (f == NULL)
	{
		printf("%s n'a pas pu être ouvert en lecture\n", "Candide_chapitre1.txt");
		return 1;
	}
	fscanf(f, "%c", &c);
	while (!feof(f))
	{
		printf("%c", c);
		fscanf(f, "%c", &c);
	}

	fclose(f);
	return 0;
}
