a
    ��Ca(  �                   @   s�   d dl T d dl mZ d dlmZ d dlmZ d dlmZ d dlZd dlZd dl	Z	dd� Z
d	d
� Zdd� Zdd� Zdd� ZG dd� de�ZG dd� de�ZdaG dd� de�Ze� ZdS )�    )�*)�ttk)�exists)�listdir)�removeNc                 C   s(   |  j d7  _ | ��  | jjdd� d S )Ni�  z The devil grants you 666 cookies��text��cookies�update_cookie_count�	CheatText�config��self� r   �main.pyw�cheat_devil   s    r   c                 C   sh   t jjdkr@t jjdkr@|  jd9  _| ��  | jjdd� d S | jjdd� |  jd7  _| ��  d S )N�   �   �   zMay the 4th be with your   zTry again later ;)�   )�datetime�dateZmonthZdayr
   r   r   r   r   r   r   r   �	cheat_4th   s    r   c                 C   s(   |  j d7  _ | ��  | jjdd� d S )N�d   zah so you like the sims eh?r   r	   r   r   r   r   �cheat_rosebud   s    r   c                 C   s<   | j jdd� | j�d� | jj| jdd� | j�d� d S )NzAYou can't read this because you threw the cheat tab into oblivionr   r   �Cheats)r   r   �TabsZforget�add�CheatsGoneTab�selectr   r   r   r   �cheat_begone$   s    r!   c                 C   s   | j jdd� d S )N� ��show)�
CheatInputr   r   r   r   r   �
cheat_show+   s    r&   c                       s�   e Zd ZdZddgZg d�Zeeee	e
gZddgZdZdZ� fdd�Zdd	� Zd
d� Zdd� Zdd� Zdd� Zdd� Zdd� Z�  ZS )�Appr   )Z666zmay the 4th be with youZrosebudzsv_cheats 0r$   r   �
   Nc                    s�  t � ��  � �d� tj� ddd�� _t� j�� _t� j�� _t� j�� _	t� j�� _
t� j�� _� jj� jdd� � jj� jdd� � jj� j	dd� � jj� jd	d� � j��  t� jd
d�� _� jjddddd� t� jd� jd�� _� jjddddd� t� j	dd�� _� jjddd� � j�d� fdd�� t� j	d� jd�� _� jjddd� t� j	dd�� _� jjdddd� t� j
dd�� _� j��  t|��r
t|d��N}t�|�}|� _|d � j k�r�|d � _!|d � _"|d � _#W d   � n1 �s 0    Y  t� j�� _$|d d!� d"k�r>� j$�%d|d d!� � � j$jddd� t� jd	� j&d�� _'� j'jddd� t� jd#d�jdddd� d� _(t)d$�D ]H}|�*d%��r�t� j|d d!� d�}|j� j(ddd� �  j(d7  _(�q�t� jd
d�� _+� j+jddd� t� jd&�,� j#d � j"d �� j-d�� _.� j.jddd� t� jd'�,� j#d � j"d �� fd(d�d�� _/� j/jddd� t0t1� j"��D ]4}|dk�r�t0� j"| �D ]}� �2d)� j3� �q��q�� �4�  d S )*Nz
Py Clickeri�  i,  )�widthZheightZClickerr   ZUpgradesr   ZSavez	0 cookiesr   r   )�row�columnZrowspan�
columnspanZClick�r   �commandr   r#   �r*   r+   z<Return>c                    s   � � � S �N)�cheat)�er   r   r   �<lambda>`   �    zApp.__init__.<locals>.<lambda>ZDonez*Enter a cheat then hit done or press enterr   �r*   r+   r,   zGone Fishing�r�saveVerr
   �upgrades�upgradeCosts�   �����ZNewGamez-- Saves --�saves�.jsonzBuy Clicker ({:d} cookies) {:d}z(Buy Better Equipment ({:d} cookies) {:d}c                      s   � � d� jd�S )Nr   zBuy Better Equipment )�buy_upgrade�UpgradeAmountr   r   r   r   r3   �   s   
��'  )5�super�__init__Zwm_titler   ZNotebookr   ZFrameZ
ClickerTabZUpgradesTabZ	CheatsTabr   �SaveTabr   Zpack�Label�CookiesCounter�grid�Button�clickZClickButtonZEntryr%   Zbindr1   ZCheatButtonr   ZGoneFishingr   �open�json�load�saveDatar7   r
   r8   r9   �SaveFile�insert�saveZ
SaveButtonr*   r   �endswith�UpgradeCookiesCounter�format�upgrade_clicker_buy�UpgradeClickerr?   �range�len�after�do_click_upgrade_betterr   )r   Zsavefile�file�dataZlabel�i�j��	__class__r   r   rB   J   s�    







*���
�
zApp.__init__c                 C   s$   |  j | jd d 7  _ | ��  d S )Nr   )r
   r8   r   r   r   r   r   rH   �   s    z	App.clickc                 C   s|   | j �� �� | jv rF| j| j�| j �� �� � | � | j �dd� d S | j �dd� | jjdd� |  j	d8  _	| �
�  d S )Nr   �endzCheater cheater pumpkin eaterr   r   )r%   �get�lower�
cheatNames�cheats�index�deleter   r   r
   r   r   r   r   r   r1   �   s     z	App.cheatc                 C   s�   | j | j| kr~|  j | j| 8  _ | ��  | j|  d7  < | j|  | j| d 7  < |j|d�| j| | j| � d� d S )Nr   r   z({:d} cookies) {:d}r   )r
   r9   r   r8   r   rR   )r   Zupgrade�buttonZbutton_formatr   r   r   r>   �   s    �zApp.buy_upgradec                 C   s0   | j jd�| j�d� | jjd�| j�d� d S )Nz{:d} cookiesr   )rE   r   rR   r
   rQ   r   r   r   r   r   �   s    zApp.update_cookie_countc                 C   s   | � �  | �d| j� d S )Nr@   )rH   rW   rX   r   r   r   r   rX   �   s    zApp.do_click_upgrade_betterc                 C   s"   | � d| jd� | �d| j� d S )Nr   zBuy Clicker r@   )r>   rT   rW   rX   r   r   r   r   rS   �   s    zApp.upgrade_clicker_buyc              	   C   s4  t d| j��  d �s8t| j| j�� d�j| jddd� td| j��  d d��2}tj	| j
| j| j| jd�|d	d
� W d   � n1 s�0    Y  td| j��  d d��t}td| j��  d d��:}t�� }|�t|�� d�� |�|�� � W d   � n1 �s0    Y  W d   � n1 �s&0    Y  d S )N�saves/r=   r   r   r   r5   �w)r7   r
   r8   r9   r   )�indent�.hash�wbr6   �utf-8)r   rM   r`   rD   rC   rF   r*   rI   rJ   �dumpr7   r
   r8   r9   �hashlib�md5�update�bytes�read�write�digest)r   rY   �hashfile�
fsdgsdghsdr   r   r   rO   �   s     "��$zApp.save)�__name__�
__module__�__qualname__r
   r8   rb   r   r   r   r!   r&   rc   r9   r7   rL   rB   rH   r1   r>   r   rX   rS   rO   �__classcell__r   r   r]   r   r'   /   s0   ���H
	r'   c                   @   s&   e Zd Zd	dd�Zdd� Zdd� ZdS )
�SaveFileButtonsN�NewGame.jsonc                 C   sB   t ||d d� | jd�| _t |d| jd�| _|| _|| _|| _d S )Nr;   r-   ZDelete)rG   r    �selectButton�	delselect�deleteButtonr.   �
delcommandrY   )r   ZmasterrY   r.   r�   r   r   r   rB   �   s
    zSaveFileButtons.__init__c                 C   s   | j d ur| � | � d S r0   )r.   r   r   r   r   r    �   s    
zSaveFileButtons.selectc                 C   s   | j d ur| � | � d S r0   )r�   r   r   r   r   r~   �   s    
zSaveFileButtons.delselect)Nr|   NN)rw   rx   ry   rB   r    r~   r   r   r   r   r{   �   s   
r{   c                       s8   e Zd Zg Z� fdd�Zdd� Zdd� Zdd� Z�  ZS )	�SaveFilePickerc           	   
      s�  t � ��  | �dd� t| d| jd�jddd� td�}g }|D ]�}|�d�sPq@td| d	���}t	�
� }|�t|�� d
�� td|d d�  d �s�W d   � q@td|d d�  d d��8}|�� }|�� |kr�|�|� ntd� W d   � n1 s�0    Y  W d   � q@1 �s0    Y  q@tt|��D ]X}| j�t| || | j| j�� | jd jj|d dd� | jd jj|d dd� �q2| ��  d S )N��   r   zNew Gamer-   r/   r<   r=   rg   r6   rl   r;   rj   �rbzfile failed hash check�����r   )rA   rB   ZminsizerG   �start_new_gamerF   r   rP   rI   rn   ro   rp   rq   rr   r   rt   �append�printrU   rV   �buttonsr{   �start�del_commandr}   r   �mainloop)	r   Zfilesa�filesrY   Zfiledatarv   ru   Z	inputhashr[   r]   r   r   rB   �   s.    

HzSaveFilePicker.__init__c                 C   s"   t d|j �a| ��  t��  d S )Nrg   )r'   rY   �app�destroyr�   �r   rf   r   r   r   r�   �   s    zSaveFilePicker.startc                 C   s   t d�a| ��  t��  d S )Nr|   )r'   r�   r�   r�   r   r   r   r   r�   �   s    zSaveFilePicker.start_new_gamec                 C   s@   |j ��  |j��  td|j � td|jd d�  d � d S )Nrg   r;   rj   )r}   Zgrid_forgetr   r   rY   r�   r   r   r   r�     s    

zSaveFilePicker.del_command)	rw   rx   ry   r�   rB   r�   r�   r�   rz   r   r   r]   r   r�   �   s
   r�   )Ztkinterr   �os.pathr   �osr   r   r   rJ   rn   r   r   r   r!   r&   ZTkr'   r{   r�   r�   Z
savePickerr   r   r   r   �<module>   s$    0