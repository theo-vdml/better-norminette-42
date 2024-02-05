# betternorm/betternorm.py

import subprocess
from colorama import init, Fore, Style
import argparse

# Initialisation de colorama
init(autoreset=True)

def colorize_line_old(output_line):
    # Vérifiez si la ligne correspond à un motif OK
    if ": OK!" in output_line:
        return f"{Fore.GREEN}{output_line}{Style.RESET_ALL}"

    # Vérifiez si la ligne correspond à un motif Error
    elif ": Error!" in output_line:
        return f"{Fore.RED}{output_line}{Style.RESET_ALL}"

    # Vérifiez si la ligne correspond à un motif Error avec détails
    elif "Error:" in output_line:
        # Utilisez différentes couleurs pour les composants spécifiés
        output_line = output_line.replace("Error:", f"{Fore.YELLOW}Error:{Fore.CYAN}")
        output_line = output_line.replace("(line:", f"{Fore.YELLOW}(line:")
        output_line = output_line.replace("):", f"):{Style.RESET_ALL}")
        return output_line

    # Par défaut, renvoie la ligne inchangée
    return output_line

import os
from colorama import Fore, Style

def colorize_line(output_line, minimize=False):
    # Extraire le nom du fichier depuis le chemin complet si présent
    file_name = "joke"
    if minimize and (": OK!" in output_line or ": Error!" in output_line):
        path_start = 0
        path_end = output_line.find(":")
        if path_start != -1 and path_end != -1:
            path = output_line[path_start:path_end]
            file_name = os.path.basename(path)  # Extraction du nom du fichier

    # Vérifie si la ligne correspond à un motif OK
    if ": OK!" in output_line:
        if minimize:
            return f"{Fore.GREEN}{file_name}: OK!{Style.RESET_ALL}"
        return f"{Fore.GREEN}{output_line}{Style.RESET_ALL}"

    # Vérifie si la ligne correspond à un motif Error
    elif ": Error!" in output_line:
        if minimize:
            return f"{Fore.RED}{file_name}: Error!{Style.RESET_ALL}"
        return f"{Fore.RED}{output_line}{Style.RESET_ALL}"

    # Vérifie si la ligne correspond à un motif Error détaillé
    elif "Error:" in output_line:
        if minimize:
            # Extraction et formatage des détails de l'erreur pour la version minimisée
            parts = output_line.split()
            line_number = parts[3].replace(",", "").replace(")", "").replace(":", "")
            col_number = parts[5].replace(",", "").replace(")", "").replace(":", "")
            error_name = parts[1]
            # Construction du message minimisé
            minimized_message = f"({Fore.CYAN}{line_number}{Style.RESET_ALL}:{Fore.CYAN}{col_number}{Style.RESET_ALL}):  \t{Fore.YELLOW}{error_name}{Style.RESET_ALL}"
            return minimized_message
        else:
            output_line = output_line.replace("Error:", f"{Fore.YELLOW}Error:{Fore.CYAN}")
            output_line = output_line.replace("(line:", f"{Fore.YELLOW}(line:")
            output_line = output_line.replace("):", f"):{Style.RESET_ALL}")
            return output_line

    # Par défaut, renvoie la ligne inchangée
    return output_line


def main():

    parser = argparse.ArgumentParser(description="Execute norminette and output with colorization.")
    parser.add_argument("filename", nargs="?", help="Optional filename to be passed to norminette.")
    parser.add_argument("-a", "--args", nargs=argparse.REMAINDER, help="Take the rest of the command as additional arguments for norminette.")
    parser.add_argument("-e", "--error-only", action="store_true", help="Shows erros only")
    parser.add_argument("-m", "--minimize", action="store_true", help="Shows minimized output")
    parser.add_argument("-s", "--summary-only", action="store_true", help="Shows only summary (with errors files names)")
    # Ajoutez d'autres arguments selon vos besoins
    
    args = parser.parse_args()

    # Si -e est spécifié, affiche un message d'exemple

    cmd = ["norminette"]
        
    if args.filename:
        cmd.append(args.filename)
        
    if args.args:
        cmd.extend(args.args)

    print(f"{Fore.CYAN}[CMD] Executing :{Style.RESET_ALL} {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    files_ok = []
    files_ko = []
    errors = []
    files_ko_and_errors = []
    for line in result.stdout.split("\n"):
        if ": OK!" in line:
            files_ok.append(line)
        elif ": Error!" in line:
            files_ko.append(line)
            files_ko_and_errors.append(line)
        elif "Error:" in line:
            errors.append(line)
            files_ko_and_errors.append(line)
    
    if len(files_ok) > 0 and not args.error_only and not args.summary_only:
        print(f"{Fore.GREEN}\n=====[ NORM OK ]====={Style.RESET_ALL}\n")

        for line in files_ok:
            print(colorize_line(line, args.minimize))

        print("\n")

    if len(files_ko_and_errors) > 0 and not args.summary_only:
        print(f"{Fore.RED}\n=====[ NORM KO ]====={Style.RESET_ALL}\n")


        for line in files_ko_and_errors:
            if ": Error!" in line:
                print("\n" + colorize_line(line, args.minimize) + "\n")
            else:
                print(colorize_line(line, args.minimize))

        print("\n")

    print(f"{Fore.CYAN}\n=====[ SUMMARY ]====={Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}Correct files:{Style.RESET_ALL} {len(files_ok)}")
    print(f"{Fore.RED}Files containing errors:{Style.RESET_ALL} {len(files_ko)}")
    print(f"{Fore.YELLOW}Errors count:{Style.RESET_ALL} {len(errors)}")
    if args.summary_only:
        print(f"{Fore.WHITE}\nErrors are in following files:{Style.RESET_ALL}")
        for file in files_ko:
            print(f"- {Fore.RED}{file.replace(': Error!', '')}{Style.RESET_ALL}")
if __name__ == "__main__":
    main()