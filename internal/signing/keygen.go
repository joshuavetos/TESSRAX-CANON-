FILE: internal/signing/keygen.go

package signing

import (
	"crypto/ed25519"
	"crypto/rand"
	"errors"
	"os"
	"path/filepath"
)

// GenerateKeypair creates a raw Ed25519 keypair.
// Private key is 64 bytes. Public key is 32 bytes.
// Files are written with strict permissions.
func GenerateKeypair(outPath string) error {
	if outPath == "" {
		return errors.New("output path required")
	}

	pub, priv, err := ed25519.GenerateKey(rand.Reader)
	if err != nil {
		return err
	}

	privPath := outPath
	pubPath := outPath + ".pub"

	if err := os.WriteFile(privPath, priv, 0600); err != nil {
		return err
	}
	if err := os.WriteFile(pubPath, pub, 0644); err != nil {
		return err
	}

	return nil
}

FILE: cmd/forensic-probe/keygen.go

package main

import (
	"flag"
	"fmt"
	"os"

	"forensic-probe/internal/signing"
)

func runKeygen(args []string) {
	fs := flag.NewFlagSet("keygen", flag.ExitOnError)
	out := fs.String("out", "", "output path for private key (public key saved as .pub)")
	fs.Parse(args)

	if *out == "" {
		fmt.Println("ERROR: --out is required")
		os.Exit(1)
	}

	if err := signing.GenerateKeypair(*out); err != nil {
		fmt.Println("KEYGEN FAILED:", err)
		os.Exit(1)
	}

	fmt.Println("KEYGEN OK")
	fmt.Println("PRIVATE KEY:", *out)
	fmt.Println("PUBLIC KEY :", *out+".pub")
}

FILE: cmd/forensic-probe/main.go (ADD DISPATCH)

switch os.Args[1] {
case "keygen":
	runKeygen(os.Args[2:])
case "capture":
	runCapture(os.Args[2:])
case "verify":
	runVerify(os.Args[2:])
default:
	usage()
	os.Exit(1)
}

STATUS: SHIPPED
ACTIONABLE: YES
