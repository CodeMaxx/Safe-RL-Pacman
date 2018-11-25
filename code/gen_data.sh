#!/bin/bash

declare -a algorithm_list=("ApproximateQAgent" "PacmanQAgent")
declare -a horizon_list=(2000)
declare -a instance_grid_list=("smallGrid")

for algorithm in "${algorithm_list[@]}"
do
	echo "$algorithm"
	for horizon in "${horizon_list[@]}"
	do
		echo "	$horizon"
		for instance in "${instance_grid_list[@]}"
		do
			echo "		$instance"
			python pacman.py -p $algorithm -x $horizon -n $horizon -l $instance -s -g DirectionalGhost > ../data/$algorithm-$instance-shield-intelligent-$horizon.dat
			python pacman.py -p $algorithm -x $horizon -n $horizon -l $instance -g DirectionalGhost > ../data/$algorithm-$instance-normal-intelligent-$horizon.dat
		done
	done
done