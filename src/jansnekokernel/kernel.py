##!/usr/bin/env python
from ipykernel.kernelbase import Kernel
import pexpect, os, shutil

workingdir = "/tmp/nekocode/"

class jansnekokernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.10.0'
    language = 'neko'
    language_version = '2.3.0'
    language_info = {
        'name': 'neko',
        'mimetype': 'application/neko',
        'file_extension': '.neko',
    }
    banner = "neko kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            if os.path.exists(workingdir):
                shutil.rmtree(workingdir)
            os.mkdir(workingdir)
            with open(workingdir + "project.neko", "w") as f:
                    f.write(code)
            solution = pexpect.run('nekoc ' + workingdir  + 'project.neko')
            if os.path.exists(workingdir + 'project.n'):
                solution = pexpect.run('neko ' + workingdir + 'project.n').decode('ascii')
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
    
    def do_shutdown(self, restart):
        if os.path.exists(workingdir):
            shutil.rmtree(workingdir)
