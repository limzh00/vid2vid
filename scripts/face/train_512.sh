python3.6 train.py --name edge2face_512 \
--dataroot datasets/face/ --dataset_mode face \
--input_nc 15 --loadSize 512 --num_D 3 \
--gpu_ids 1,2,3 --n_gpus_gen 3 \
--niter 200 --niter_decay 200 --n_frames_total 12 \
--batchSize 4 --continue_train --no_html \
--save_epoch_freq 20