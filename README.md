# MO436_DRL
Projeto 2 da Disciplina MO436 (Topics in Machine Learning - Reinforcement Learning)




Resultados usando Ms. Pacman:


PPO




DQN

Para o experimento I, testamos alguns parametros (descritos na tabela abaixo) e os demais congelamos durante as simulações: learning_starts: 50000,train_freq:4
gradient_steps:1,n_episodes_rollout:-1,optimize_memory_usage: FALSO,exploration_initial_eps:1,exploration_final_eps:0.05,max_grad_norm:10,'tensorboard_log: none, create_eval_env:falso, verbose:0, seed: 1278,device:auto
_init_setup_model:verdadeiro.

| id | lr | buffer_size | batch_size | tau | gamma ($\gamma$) | exploration_fraction | Tempo (segundos) | Média | Desvio
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 1 | 0.0005 | 10000 | 32 | 0.2 | 0.99 | 0.1 | 18680.38 | 1688.0 | 709.7 |
| 2 | 0.0005 | 10000 | 32 | 0.5 | 0.99 | 0.7 | 17176.83 | 1759.3 | 693.7 |
| 3 | 0.0005 | 10000 | 32 | 0.5 | 0.99 | 0.5 | 19301.75 | 1400.6 | 545.8 |
| 4 | 0.0005 | 10000 | 32 | 0.5 | 0.99 | 0.1 | 18451.75 | 1990.0| 966.3 |
| 5 | 0.00005 | 10000 | 32 | 0.5 | 0.2 | 0.1 | 14929.69 | 573.3 | 255.0 |
| 6 | 0.00005 | 20000 | 32 | 0.5 | 0.2 | 0.1 | 15679.66 | 374.6 | 222.0 |
| 7 | 0.00005 | 20000 | 64 | 0.5 | 0.2 | 0.1 | 16897.80 | 687.3 | 556.5|


Resultados usando Cartpole:




PPO




DQN






