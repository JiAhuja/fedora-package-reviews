Name:           python-mcp-security-scanner
Version:        0.1.5
Release:        %autorelease
Summary:        Model Context Protocol (MCP) server for security scanning

License:        Apache-2.0
URL:            https://pypi.org/project/mcp-security-scanner
Source:         %{pypi_source mcp_security_scanner}

BuildArch:      noarch
BuildRequires:  python3-devel
# below packages required for test execution
BuildRequires:  python3-fastapi
BuildRequires:  python3-uvicorn


%global _description %{expand:
This is a Python-based penetration testing tool for Model Context
Protocol (MCP) servers. It supports HTTP, stdio, and experimental
SSE transports, runs a suite of checks mapped to scanner_specs.schema
(authentication, transport, tools, prompts, resources), and includes a
deliberately insecure MCP-like server for testing.}

%description %_description

%package -n     python3-mcp-security-scanner
Summary:        %{summary}

%description -n python3-mcp-security-scanner %_description


%prep
%autosetup -p1 -n mcp_security_scanner-%{version}
sed -i 's/license = { file = "LICENSE" }/license-files = ["LICENSE"]/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l insecure_mcp_server mcp_scanner


%check
%pyproject_check_import

%files -n python3-mcp-security-scanner -f %{pyproject_files}
%{_bindir}/insecure-mcp-server
%{_bindir}/mcp-scan


%changelog
%autochangelog
