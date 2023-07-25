time=$(date "+%Y%m%d-%H%M%S").log
nohup ./clash -d . >$time &
