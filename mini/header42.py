
import os

CONFIG_PATH = os.path.expanduser("~/.mini42")

def save_config(user, campus):
    with open(CONFIG_PATH, "w") as f:
        f.write(user + "\n")
        f.write(campus + "\n")
        
def load_config():
    if not os.path.exists(CONFIG_PATH):
        return None, None
    with open(CONFIG_PATH, "r") as f:
        lines = f.read().splitlines()[0:2]
        return lines[0] if len(lines) > 0 else None, lines[1] if len(lines) > 1 else None

def clear_config():
    if os.path.exists(CONFIG_PATH):
        os.remove(CONFIG_PATH)

def build_header(file_name):
    user, campus = load_config()
    if user is None or campus is None:
        return None
    by: str = f"By: {user} <{user}@student.42{campus.lower()}.com>"
    return [
        "/* ************************************************************************** */",
        "/*                                                                            */",
        "/*                                                        :::      ::::::::   */",
        f"/*   {file_name.ljust(51)}:+:      :+:    :+:   */",
        "/*                                                    +:+ +:+         +:+     */",
        f"/*   {by.ljust(47)[:47]}+#+  +:+       +#+        */",
        "/*                                                +#+#+#+#+#+   +#+           */",
        f"/*   Created: 2026/10/03 12:54:32 by {user.ljust(8)}          #+#    #+#             */",
        f"/*   Updated: 2026/10/03 13:58:56 by {user.ljust(8)}         ###   ########.fr       */",
        "/*                                                                            */",
        "/* ************************************************************************** */",
    ]