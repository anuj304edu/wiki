from django.shortcuts import render

from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse



def search(request):
    if request.method == "GET":
        title = request.GET.get("q", "")
        list_entry = util.list_entries()
        if title in list_entry:
            return render(request, "encyclopedia/s_entry.html",{
            "s_title": title,
            "s_entry": util.get_entry(title)
            })
        elif title != "":
            list_q = [i for i in list_entry if title.casefold() in i.casefold()]
            return render(request, "encyclopedia/results.html",{
                    "entries": list_q
                })
        else:
            return HttpResponseRedirect(reverse("index"))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def s_entry(request, title):
    return render(request, "encyclopedia/s_entry.html", {
        "s_title": title,
        "s_entry": util.get_entry(title)
    })

def createnewpage(request):
        if request.method == "POST":
            ptitle = request.POST.get("pagetitle", "")
            pcontent = request.POST.get("pagecontent", "")
            list_entry = util.list_entries()
            if ptitle in list_entry:
                return render(request, "encyclopedia/createnewpage.html", {
                    "Title": ptitle
                })
            elif ptitle != "":
                util.save_entry(ptitle, pcontent)
                return render(request, "encyclopedia/s_entry.html", {
                    "s_title": ptitle,
                    "s_entry": util.get_entry(ptitle)
                    })
            else:
                return HttpResponseRedirect(reverse("createnewpage"))
        else:
            return render(request, "encyclopedia/createnewpage.html")


def editpage(request, title):
    if request.method == "POST":
            ptitle = request.POST.get("pagetitle")
            pcontent = request.POST.get("pagecontent")
            if ptitle != "":
                list_entry = util.list_entries()
                atitle = util.edit_entry(title, ptitle, pcontent)
                if atitle in list_entry:
                    return render(request, "encyclopedia/editpage.html", {
                        "s_title": ptitle,
                        "s_entry": pcontent,
                        "Title": atitle
                        })
                else:
                    return render(request, "encyclopedia/s_entry.html", {
                    "s_title": ptitle,
                    "s_entry": pcontent
                    })
    else:
        return render(request, "encyclopedia/editpage.html", {
        "s_title": title,
        "s_entry": util.get_entry(title)
    })

def deletepage(request, title):
    if request.method == "POST":
        util.delete_entry(title)
        return HttpResponseRedirect(reverse("index"))
