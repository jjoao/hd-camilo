import ColemanLiau_index as func
import untag_xml as untag


def gerarGrade(ficheiro='./CASTELO-BRANCO,Camilo-AmorDePerdição.txt'):
    with open(ficheiro, 'r', encoding='utf-8') as textfile:
        print('Grade:', func.colemanLiau(textfile.read()))
        print('-'*30)
        print('\tIndex Score:')
        print('-'*30)
        print('5 & below: Very easy to read\n'
              '6: Easy to read\n'
              '7: Fairly easy to read\n'
              '7-10: Conversational English\n'
              '11-12: Fairly difficult to read\n'
              '13-16: Difficult to read\n'
              '17+: Extremely difficult to read')
        print('-'*30)


def gerarGradeXML(ficheiro='./CASTELO-BRANCO,Camilo-AmorDePerdição.xml'):
    with open(ficheiro, 'r', encoding='utf-8') as xml_file:
        xml = xml_file.read()
        print('Grade:', func.colemanLiau(untag.untag(xml)))
        print('-'*30)
        print('\tIndex Score:')
        print('-'*30)
        print('5 & below: Very easy to read\n'
              '6: Easy to read\n'
              '7: Fairly easy to read\n'
              '7-10: Conversational English\n'
              '11-12: Fairly difficult to read\n'
              '13-16: Difficult to read\n'
              '17+: Extremely difficult to read')
        print('-'*30)


ficheiro = input('Choose your file: ')
escolha = int(input('Choose file type: \n'
                    '1' + ' ' + 'txt \n'
                    '2' + ' ' + 'xml \n '))
if escolha == 1:
    gerarGrade(ficheiro)
elif escolha == 2:
    gerarGradeXML(ficheiro)
else:
    print('Erro!')
