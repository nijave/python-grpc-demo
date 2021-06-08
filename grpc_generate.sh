#!/bin/bash

OUTDIR=.

python -m grpc_tools.protoc \
	-Iprotobufs/ \
	--python_out="$OUTDIR" \
	--grpc_python_out="$OUTDIR" \
	protobufs/*/*.proto
