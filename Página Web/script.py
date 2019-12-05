import numpy as np
import pandas as pd 
from pandas import DataFrame
from sklearn.ensemble import AdaBoostClassifier
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, KernelPCA
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
import joblib

#Asignación de joblibs
one_hot_localizacion = joblib.load('one_hot_localizacion.joblib')
encoder_sexo = joblib.load('encoder_sexo.joblib')
encoder_multiple = joblib.load('encoder_multiple.joblib')
encoder_uci = joblib.load('encoder_uci.joblib')
historicos_pca = joblib.load('historicos_pca.joblib')
historicos_kmean = joblib.load('historicos_kmean.joblib')
ada_clf = joblib.load('ada_clf.joblib')
graph_kpca = joblib.load('graph_kpca.joblib')
graph_kmean = joblib.load('graph_kmean.joblib')
features_graph1 = ["edad","sexo","gcs","tamano","fihser_num"]


features = ["edad", "sexo", "multiple", "gcs", "wfns_pretratamiento_num", "wfns_ingreso_num",
            "fihser_num", "tamano", "uci", "Oct_12", "momento_num", "localizacion"]

train_labels = ["edad", "sexo", "gcs", "wfns_pretratamiento_num", "wfns_ingreso_num", "fihser_num", "tamano", "uci", "Oct_12", "momento_num",
                'A.Ch.A: Arteria coroidea anterior',
                'A.Co.P: Arteria comunicante posterior',
                'ACA: Arteria cerebral anterior', 'ACI: Arteria carotida interna',
                'ACM: Arteria cerebral media', 'ACP: Arteria cerebral posterior',
                'ACoA: Arteria comunicante anterior', 'BAS: Apex de la basilar',
                'BIF: Bifurcacion carotidea', 'OFT: Arteria oftalmica',
                'PERI: Pericallosa', 'PICA', 'VBA: Vertebrobasilar: AICA, SCA',"historicos_mat"]

historicos_features = ['HTA', 'tabaq', 'obesidad',
                       'diabetes', 'alcohol', 'drogas', 'familiares']


paciente1 = [65, "Hombre", "Si", 12, 5, 4, 2, 7, "Si",
             0, 2, "A.Co.P: Arteria comunicante posterior"]
historicos1 = [1, 0, 0, 0, 0, 0, 0]


def runPatient(paciente, historico):
    paciente = pd.DataFrame([paciente], columns=features)
    paciente.sexo = encoder_sexo.transform(paciente[["sexo"]])
    paciente.multiple = encoder_multiple.transform(paciente[["multiple"]])
    paciente.uci = encoder_uci.transform(paciente[["uci"]])
    loc_hot = one_hot_localizacion.transform(paciente["localizacion"].values.reshape(-1, 1))
    loc_hot_df = pd.DataFrame(loc_hot, columns=one_hot_localizacion.categories_[0])
    paciente = paciente.join(loc_hot_df, how="left")
    paciente.drop(["localizacion"], axis=1)
    historicos = pd.DataFrame([historico], columns=historicos_features)
    trans_historicos = historicos_pca.transform(historicos[historicos_features])
    kmean_scale = historicos_kmean.predict(trans_historicos)
    paciente["historicos_mat"] = kmean_scale
    prediccion_prob = ada_clf.predict_proba(paciente[train_labels])
    prediccion = ada_clf.predict(paciente[train_labels])
    features_kpca = graph_kpca.transform(paciente[features_graph1])
    label_kmean = graph_kmean.predict(features_kpca)
    ret0 = str(round(prediccion_prob[0][0] * 100, 2)) + ' %'
    ret1 = str(round(prediccion_prob[0][1] * 100, 2)) + ' %'
    ret2 = prediccion[0]
    if (ret2 == 0):
        ret2 = 'Quirúrgico'
    else:    
        ret2 = 'Endovascular'    
    ret3 = round(trans_historicos[0][0], 4)
    ret4 = round(trans_historicos[0][1], 4)
    ret5 = kmean_scale[0]
    ret6 = round(features_kpca[0][0], 4)
    ret7 = round(features_kpca[0][1], 4)
    ret8 = round(features_kpca[0][2], 4)
    ret9 = label_kmean[0]
    salida = [ret0, ret1, ret2, ret3, ret4, ret5, ret6, ret7, ret8, ret9]
    return salida   
