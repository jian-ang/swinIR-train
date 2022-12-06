python -m torch.distributed.launch --nproc_per_node=2 --master_port=1234 main_train_psnr.py --opt options/swinir/train_swinir_sr_classical.json

python -m torch.distributed.launch --nproc_per_node=2 main_train_psnr.py --opt options/swinir/train_swinir_sr_classical.json

python -m pdb main_train_psnr.py --opt options/swinir/train_swinir_sr_classical.json

python main_train_psnr.py --opt options/swinir/train_swinir_sr_classical.json

python main_train_gan.py --opt options/swinir/train_swinir_sr_realworld_x4_gan.json

# b <line num> --> breakpoint
# c --> continue
# up --> moves up the callstack
# l --> lists a few lines near current statement
# ll --> lists whole function (long list)
# p <expr> --> print value of expr
# ? --> get help
# n --> step over
# s --> step into
# r --> step out

# testing
python main_test_swinir.py --task classical_sr --scale 8 --training_patch_size 48 --model_path model_zoo/swinir/001_classicalSR_DIV2K_s48w8_SwinIR-M_x8.pth --folder_lq testsets/WIN/test-LRx8-100 --folder_gt testsets/WIN/test-HR-100

python main_test_swinir.py --task classical_sr --scale 8 --training_patch_size 48 --model_path model_zoo/swinir/003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth --folder_lq testsets/WIN/test-LRx8-100 --folder_gt testsets/WIN/test-HR-100

python main_test_swinir.py --task real_sr --scale 4 --model_path model_zoo/swinir/003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth --folder_lq testsets/WIN/WIN/test-LRx8-100 --tile