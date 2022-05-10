from experiment_utils import *
from params_distribution_disruption_high_unc import *


## HMM init
hmm = HMM(n_components=3, n_obs=6 )
hmm.emissionprob_ = hmm_params['emission']
hmm.transmat_     = hmm_params['transition']
hmm.startprob_    = hmm_params['priors']


res_d = all_experiments_loop(X_obs, hmm, problem_dict, unc_dict, params_dict)


ratio_df = ratio_results_to_df(res_d)
contour_df = contour_results_to_df(res_d)
box_df = box_results_to_df(res_d)
info_df = info_results_to_df(res_d)


problem_dir = 'results_prueba/distribution_disruption/dd_high_unc'

ratio_df.to_csv(problem_dir+'_ratio.csv', index = False)
contour_df.to_csv(problem_dir+'_contour.csv', index = False)
box_df.to_csv(problem_dir+'_box.csv', index = False)
info_df.to_csv(problem_dir+'_info.csv', index = False)