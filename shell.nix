let
  pkgs = import <nixpkgs> {};
  roundingsat = pkgs.callPackage ./roundingsat.nix {};
in
  pkgs.mkShell {
    buildInputs = [ roundingsat ];
  }
