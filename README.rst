The ``conda`` command is the primary interface for managing an Anaconda installations. It can query and search the Anaconda package index and current Anaconda installation, create new Anaconda environments, and install and upgrade packages into existing Anaconda environments.


========
Examples
========

Create an Anaconda environment called ``myenv`` containing the latest version of scipy and all dependencies.

.. code-block:: bash
    
    $ conda create -n myenv scipy

Install the latest version of pandas into ``myenv``

.. code-block:: bash

    $ conda install -n myenv pandas

Update all specified packages to latest versions in ``myenv``

.. code-block:: bash

    $ conda update -n myenv anaconda

=======
License
=======

Except where noted in LICENSE.txt, ``conda`` is released under the following terms:

.. code-block::

       (c) 2012 Continuum Analytics, Inc. / http://continuum.io
       All Rights Reserved
    
       Redistribution and use in source and binary forms, with or without
       modification, are permitted provided that the following conditions are met:
     * Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.
     * Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.
     * Neither the name of Continuum Analytics, Inc. nor the
       names of its contributors may be used to endorse or promote products
       derived from this software without specific prior written permission.
    
     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
     ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
     WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
     DISCLAIMED. IN NO EVENT SHALL CONTINUUM ANALYTICS BE LIABLE FOR ANY
     DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
     (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
     LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
     ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
     (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
     SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.