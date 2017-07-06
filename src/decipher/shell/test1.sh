#!/bin/sh

function initSources(){
	sourceConfig='10030|Applift_Affiliate_C,10090|Glispa_Affiliate_D'
	echo -e $sourceConfig
}

initSources
sources=$(echo -e `initSources`)
echo $sources
