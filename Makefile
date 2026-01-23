BINARY_NAME := forensic-probe
CMD_DIR := ./cmd/forensic-probe
BUILD_DIR := ./build
VERSION := v0.1.0-alpha

GOOS ?= linux
GOARCH ?= amd64

LDFLAGS := -s -w -X main.ProbeVersion=$(VERSION)

.PHONY: all clean build build-static verify fmt

all: build

build:
	mkdir -p $(BUILD_DIR)
	GOOS=$(GOOS) GOARCH=$(GOARCH) \
	go build -trimpath -ldflags "$(LDFLAGS)" \
	-o $(BUILD_DIR)/$(BINARY_NAME) \
	$(CMD_DIR)

build-static:
	mkdir -p $(BUILD_DIR)
	CGO_ENABLED=0 GOOS=$(GOOS) GOARCH=$(GOARCH) \
	go build -trimpath -ldflags "$(LDFLAGS)" \
	-o $(BUILD_DIR)/$(BINARY_NAME)-static \
	$(CMD_DIR)

verify:
	go test ./...

fmt:
	go fmt ./...

clean:
	rm -rf $(BUILD_DIR)
