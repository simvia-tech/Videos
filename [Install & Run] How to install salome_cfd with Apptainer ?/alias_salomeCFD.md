# Alias to run Salome_CFD for Singularity or Apptainer

if [ -z "$SINGULARITY_CONTAINER" ] && [ -z "$APPTAINER_CONTAINER" ]; then
salome_cfd() {
    local sif="$HOME/path/to/SALOME_CFD_2026.sif"    # <-- path to the downloaded .sif
    local rc="$HOME/.salomecfd_bashrc"

    # Clean run command used by all  interactive shells inside the container
    [ -f "$rc" ] || printf 'PS1="[salomecfd] \\w \\$ "\n' > "$rc"

    local opts=(--cleanenv --writable-tmpfs
                --env DISPLAY="${DISPLAY:-:0}"
                --env XDG_CACHE_HOME=/tmp/.cache
                --bind /tmp/.X11-unix:/tmp/.X11-unix)           # works even if site sets "mount tmp = no"

    # Hide the user's ~/.bashrc (and the aliases/functions it defines) inside the container
    [ -f "$HOME/.bashrc" ] && opts+=(--bind "$rc":"$HOME/.bashrc")

    if grep -qi microsoft /proc/version; then
        opts+=(--env LIBGL_ALWAYS_SOFTWARE=1)                  # WSL
    elif command -v nvidia-smi >/dev/null 2>&1; then
        opts+=(--nv)                                           # native Linux + NVIDIA
    else
        opts+=(--env LIBGL_ALWAYS_SOFTWARE=1)                  # AMD/Intel/no GPU: safe software GL
    fi

    case "$1" in
        "")    set -- salome ;;
        shell) shift; set -- bash --norc --noprofile "$@" ;;
    esac

    singularity exec "${opts[@]}" "$sif" "$@"
}
fi
