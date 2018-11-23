#!/bin/bash

declare -a algorithm_list=("ApproximateQAgent" "PacmanQAgent")
declare -a horizon_list=(1000 2000)
# declare -a instance_grid_list=("smallGrid" "smallClassic" "mediumGrid")
declare -a instance_grid_list=("smallGrid" "mediumGrid")

for algorithm in "${algorithm_list[@]}"
do
	echo "$algorithm"
	for horizon in "${horizon_list[@]}"
	do
		echo "	$horizon"
		for instance in "${instance_grid_list[@]}"
		do
			echo "		$instance"
			python pacman.py -p $algorithm -x $horizon -n $horizon -l $instance -s > data/$algorithm-$instance-shield-$horizon.dat
			python pacman.py -p $algorithm -x $horizon -n $horizon -l $instance > data/$algorithm-$instance-normal-$horizon.dat
		done
	done
done