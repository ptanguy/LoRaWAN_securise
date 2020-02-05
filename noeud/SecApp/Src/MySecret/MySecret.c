/*
 * MySecret.c
 *
 *  Created on: 4 févr. 2020
 *      Author: arthur
 */


#include "MySecret.h"

unsigned char MySecret_fct(unsigned char number){
	if (256 > (number*number)){
		return number*number;
		}
	else{
		return 0;
		}
}
