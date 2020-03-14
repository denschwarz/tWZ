import ROOT

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance

@singleton
class color():
  pass

color.data           = ROOT.kBlack
color.DY             = ROOT.kBlue-9
color.TTJets         = 7
color.nonprompt      = ROOT.kBlue-9
color.singleTop      = 40
color.TTX_rare       = ROOT.kRed-10
color.TTH            = ROOT.kRed-10
color.TWZ            = ROOT.kRed
color.TTZ            = 91
color.TTZtoLLNuNu    = 91
color.signal         = ROOT.kOrange
color.TTZtoQQ        = 91
color.TTG            = ROOT.kRed
color.TTG_signal     = 91
color.TZQ            = 9
color.TWZ            = ROOT.kBlue-4
color.WJetsToLNu     = ROOT.kRed-10
color.diBoson        = ROOT.kOrange
color.multiBoson     = ROOT.kOrange
color.ZZ             = ROOT.kGreen+3
color.WZ             = 51
color.WZ_amc         = 51
color.WW             = ROOT.kOrange-7
color.VV             = 30
color.WG             = ROOT.kOrange-5
color.triBoson       = ROOT.kYellow
color.rare_noZZ      = 8
color.WZZ            = ROOT.kYellow
color.WWG            = ROOT.kYellow-5
color.QCD            = 46
