; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Autorenamer"
#define MyAppVersion "1.0.1"
#define MyAppPublisher "Melvins Corp"
#define MyAppURL "https://www.melvinsbro.com/"
#define MyAppExeName "Autorenamer 6.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{781D10A6-FC90-4DBC-BDB7-6D8894F18516}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=G:\3D Objects\Autorenamer\dist\LICENSE.txt
;InfoBeforeFile=G:\3D Objects\PySide2 Template\dist\Informations before install.txt
;InfoAfterFile=G:\3D Objects\PySide2 Template\dist\Informations before install.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=G:\3D Objects\Autorenamer
OutputBaseFilename=Autorenamer_WINDOWS_x64_1.0.1
SetupIconFile=G:\3D Objects\Autorenamer\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "G:\3D Objects\Autorenamer\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "G:\3D Objects\Autorenamer\dist\images\*"; DestDir: "{app}/images"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "G:\3D Objects\Autorenamer\dist\fonts\*"; DestDir: "{app}/fonts"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "G:\3D Objects\Autorenamer\dist\style.qss"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
