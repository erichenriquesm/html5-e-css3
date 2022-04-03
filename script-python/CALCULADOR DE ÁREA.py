print('CALCULADOR DE USO DE TINTA E ÁREA')
larg = float(input('largura da superfície:'))
alt = float(input('altura da superfície:'))
área = larg * alt
tinta = área / 2
print(f'para pintar a superfície {larg}x{alt}, \nsua área é de {área}m² \ne é  preciso de {tinta}l de tinta')
