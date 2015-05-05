for i in $(seq 1 20); do
    python capture.py -r myTeam_submit -b baselineTeam -q >> temp_out
    echo "Run $i" >> temp_out
done

