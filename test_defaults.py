import pytest

def test_default_folderName(main) :
    assert main.m_ui.folderName.text() == "Nom du dossier"
    
def test_default_parcourirButton(main) :
    assert main.m_ui.parcourirButton.text() == "Parcourir"
    
def test_default_parcourirButton2(main) :
    assert main.m_ui.parcourirButton2.text() == ""
    
def test_default_folderNameEdit(main) :
    assert main.m_ui.folderNameEdit.text() == ""
    
def test_default_renameAllCategoriesButton(main) :
    assert main.m_ui.renameAllCategoriesButton.text() == "Renommer toutes les catégories"
    
def test_default_noFileFound(main) :
    assert main.m_ui.noFileFound.text() == "Aucune catégorie trouvée ..."