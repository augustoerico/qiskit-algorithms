#!/bin/bash

MODULE="test.transpiled_sherbrooke.minimum_eigensolvers.test_qaoa"
CLASS="TestQAOA"
#METHOD_BASE="test_qaoa"
#METHOD_BASE="test_qaoa_qc_mixer"
#METHOD_BASE="test_qaoa_qc_mixer_many_parameters"
#METHOD_BASE="test_qaoa_qc_mixer_no_parameters"
#METHOD_BASE="test_change_operator_size" # failing
#METHOD_BASE="test_qaoa_initial_point" # failing
#METHOD_BASE="test_qaoa_random_initial_point"
METHOD_BASE="test_optimizer_scipy_callable"

#for i in {1..6}; do
for i in {1..3}; do
#for i in {1..9}; do
    python -m unittest "$MODULE.$CLASS.${METHOD_BASE}_$i"
done
