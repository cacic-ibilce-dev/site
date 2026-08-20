{ self, pkgs, ... }: {
  packages = with pkgs; [
    sqlite
    zlib
    tmux
  ];
}
