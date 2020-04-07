# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: ipynb,md:myst,py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Equation test

# %% [markdown]
# ## Delimiters
#
# ### Source -- with $$
# ```
# $$
# \begin{align}
# \dot{x} & = \sigma(y-x) \\
# \dot{y} & = \rho x - y - xz \\
# \dot{z} & = -\beta z + xy
# \end{align}
# $$(eq:one)
# ```
# ### Display \$\$
#
# $$
# \begin{align}
# \dot{x} & = \sigma(y-x) \\
# \dot{y} & = \rho x - y - xz \\
# \dot{z} & = -\beta z + xy
# \end{align}
# $$(eq:one)

# %% [markdown]
# ### Source -- no \$\$
# ```
# \begin{align*}
# \dot{x} & = \sigma(y-x) \\
# \dot{y} & = \rho x - y - xz \\
# \dot{z} & = -\beta z + xy
# \end{align*}
# ```
# ### Display no $$
#
#
# \begin{align*}
# \dot{x} & = \sigma(y-x) \\
# \dot{y} & = \rho x - y - xz \\
# \dot{z} & = -\beta z + xy
# \end{align*}

# %% [markdown]
# Reference {eq}`eq:one`
#
# ## aligned equations
#
# ### align numbering single
#
# ```
# $$
# \begin{align} 
# g(X_{n}) &= g(\theta)+g'({\tilde{\theta}})(X_{n}-\theta) \notag \\
# \sqrt{n}[g(X_{n})-g(\theta)] &= g'\left({\tilde{\theta}}\right)
#   \sqrt{n}[X_{n}-\theta ] 
# \end{align} 
# $$(eq:align1)
# ```
#
# $$
# \begin{align} 
# g(X_{n}) &= g(\theta)+g'({\tilde{\theta}})(X_{n}-\theta) \notag \\
# \sqrt{n}[g(X_{n})-g(\theta)] &= g'\left({\tilde{\theta}}\right)
#   \sqrt{n}[X_{n}-\theta ] 
# \end{align} 
# $$(eq:align1)
#
# ### align numbering multiple
#
# ```
# $$
# \begin{align}
# \mathrm{Var}(\hat{\beta}) & =\mathrm{Var}((X'X)^{-1}X'y)\\
#  & =(X'X)^{-1}X'\mathrm{Var}(y)((X'X)^{-1}X')'  \tag{subtest1}\\
#  & =(X'X)^{-1}X'\mathrm{Var}(y)X(X'X)^{-1}\notag\\
#  & =(X'X)^{-1}X'\sigma^{2}IX(X'X)^{-1}\\
#  & =(X'X)^{-1}\sigma^{2}\tag{subtest2}
# \end{align}
#  $$
# ```
#
#
# $$
# \begin{align}
# \mathrm{Var}(\hat{\beta}) & =\mathrm{Var}((X'X)^{-1}X'y)\\
#  & =(X'X)^{-1}X'\mathrm{Var}(y)((X'X)^{-1}X')'  \tag{subtest1}\\
#  & =(X'X)^{-1}X'\mathrm{Var}(y)X(X'X)^{-1}\notag\\
#  & =(X'X)^{-1}X'\sigma^{2}IX(X'X)^{-1}\\
#  & =(X'X)^{-1}\sigma^{2}\tag{subtest2}
#  \end{align}
#  $$
