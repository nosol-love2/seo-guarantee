# -*- coding: utf-8 -*-
"""랜딩 원본 -> 배포본(index.html) 변환 후 푸시. 사용: python deploy.py [-m "메시지"]"""
import io, os, subprocess, sys

SRC = r"D:\solset\solcap\playbook\랜딩_신청폼.html"
HERE = os.path.dirname(os.path.abspath(__file__))
DST = os.path.join(HERE, "index.html")
HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#F2EFE7">
"""

def build():
    h = io.open(SRC, encoding="utf-8").read()
    for bad in ("api_key", "BOT_TOKEN", "8517052732"):
        if bad in h:
            raise SystemExit("배포 중단 — 비밀값으로 보이는 문자열: %s" % bad)
    i = h.index("</title>") + len("</title>")
    j = h.index('<div class="sheet">')
    out = HEAD + h[:i] + h[i:j] + "</head>\n<body>\n" + h[j:] + "\n</body>\n</html>\n"
    io.open(DST, "w", encoding="utf-8").write(out)
    return len(out.encode("utf-8"))

def run(*a):
    return subprocess.run(a, cwd=HERE, capture_output=True, text=True,
                          encoding="utf-8", errors="ignore", shell=True)

if __name__ == "__main__":
    n = build()
    msg = sys.argv[sys.argv.index("-m") + 1] if "-m" in sys.argv else "랜딩 갱신"
    run("git", "add", "-A")
    r = run("git", "-c", "user.name=nosol-love2", "-c",
            "user.email=claude1@safed.co.kr", "commit", "-m", msg)
    if "nothing to commit" in (r.stdout + r.stderr):
        print("변경 없음 — %d bytes" % n); raise SystemExit(0)
    p = run("git", "push")
    print("배포 완료 %d bytes | %s" % (n, "push OK" if p.returncode == 0 else p.stderr.strip()[:120]))
    print("https://nosol-love2.github.io/seo-guarantee/")
