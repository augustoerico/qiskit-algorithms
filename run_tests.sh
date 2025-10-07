#!/bin/bash

MODULE="test.transpiled_sherbrooke.minimum_eigensolvers.test_qaoa"
CLASS="TestQAOA"
#METHOD_BASE="test_qaoa"
METHOD_BASE="test_qaoa_qc_mixer"

for i in {1..6}; do
    python -m unittest "$MODULE.$CLASS.${METHOD_BASE}_$i"
done
