{ boost, cmake, fetchgit, lib, stdenv }:

stdenv.mkDerivation rec {
  pname = "roundingsat";
  version = "2024-06-25";

  meta = with lib; {
    description = "The pseudo-Boolean solver powered by proof complexity!";
    longDescription = "";
    homepage = "https://gitlab.com/MIAOresearch/software/roundingsat";
    license = with licenses; [ mit ];
    maintainers = with maintainers; [];
    mainProgram = "roundingsat";
  };

  src = fetchgit {
    url = "https://gitlab.com/MIAOresearch/software/roundingsat.git";
    rev = "d34b6bed0ea5e0a54189650ee5acf5fcaa6b8581";
    hash = "sha256-gr235LRpP/7tSSrcVd6S07DZjcrSI7Iz9m7OWt56HN0=";
  };

  nativeBuildInputs = [ cmake ];
  buildInputs = [ boost ];
}